// default package
// Generated 26 nov 2023 19:40:10 by Hibernate Tools 5.2.13.Final
package enginerinversed.entities;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 * Follow generated by hbm2java
 */
@Entity
@Table(name = "Follow", catalog = "kurigram")
public class Follow implements java.io.Serializable {

	private int id;
	private Integer followers;
	private Integer following;
	private Set<UserFollow> userFollows = new HashSet<UserFollow>(0);

	public Follow() {
	}

	public Follow(int id) {
		this.id = id;
	}

	public Follow(int id, Integer followers, Integer following, Set<UserFollow> userFollows) {
		this.id = id;
		this.followers = followers;
		this.following = following;
		this.userFollows = userFollows;
	}

	@Id

	@Column(name = "id", unique = true, nullable = false)
	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	@Column(name = "followers")
	public Integer getFollowers() {
		return this.followers;
	}

	public void setFollowers(Integer followers) {
		this.followers = followers;
	}

	@Column(name = "following")
	public Integer getFollowing() {
		return this.following;
	}

	public void setFollowing(Integer following) {
		this.following = following;
	}

	@OneToMany(fetch = FetchType.LAZY, mappedBy = "follow")
	public Set<UserFollow> getUserFollows() {
		return this.userFollows;
	}

	public void setUserFollows(Set<UserFollow> userFollows) {
		this.userFollows = userFollows;
	}

}
