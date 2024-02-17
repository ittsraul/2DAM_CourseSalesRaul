// default package
// Generated 26 nov 2023 19:40:10 by Hibernate Tools 5.2.13.Final
package enginerinversed.entities;
import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

/**
 * UserFollow generated by hbm2java
 */
@Entity
@Table(name = "User_Follow", catalog = "kurigram")
public class UserFollow implements java.io.Serializable {

	private UserFollowId id;
	private Follow follow;
	private User user;

	public UserFollow() {
	}

	public UserFollow(UserFollowId id, Follow follow, User user) {
		this.id = id;
		this.follow = follow;
		this.user = user;
	}

	@EmbeddedId

	@AttributeOverrides({ @AttributeOverride(name = "userId", column = @Column(name = "user_id", nullable = false)),
			@AttributeOverride(name = "followId", column = @Column(name = "follow_id", nullable = false)) })
	public UserFollowId getId() {
		return this.id;
	}

	public void setId(UserFollowId id) {
		this.id = id;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "user_id", nullable = false, insertable = false, updatable = false)
	public Follow getFollow() {
		return this.follow;
	}

	public void setFollow(Follow follow) {
		this.follow = follow;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "follow_id", nullable = false, insertable = false, updatable = false)
	public User getUser() {
		return this.user;
	}

	public void setUser(User user) {
		this.user = user;
	}

}
